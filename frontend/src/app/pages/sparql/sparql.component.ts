import {Component} from '@angular/core';
import axios, {AxiosResponse} from "axios";
import {NgFor, NgIf} from "@angular/common";
import {NavbarComponent} from "../navbar/navbar.component";

@Component({
  selector: 'app-sparql',
  standalone: true,
  imports: [
    NgFor,
    NgIf,
    NavbarComponent
  ],
  templateUrl: './sparql.component.html',
  styleUrl: './sparql.component.scss'
})
export class SparqlComponent {
  errorText = ''

// Replace these values with your Fuseki server information
  results: any

  fusekiServerUrl = 'http://localhost:3030';

  datasetName = 'ELA';

// SPARQL query example

  sparqlQuery = `
    SELECT ?subject ?predicate ?object
    WHERE {
        ?subject ?predicate ?object
    }
    LIMIT 10
`;

// Construct the SPARQL query endpoint URL

  sparqlEndpointUrl = `${this.fusekiServerUrl}/${this.datasetName}/query`;

// Function to send SPARQL query to Fuseki
  async runQuery(textarea: HTMLTextAreaElement): Promise<void> {
    this.sparqlQuery = textarea.value
    try {
      const response: AxiosResponse = await axios.post(
        this.sparqlEndpointUrl,
        `query=${encodeURIComponent(this.sparqlQuery)}`,
        {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            Accept: 'application/json',
          },
        }
      );
      console.log(response)
      // Check the response
      if (response.status === 200) {
        this.results = response.data.results.bindings;
        console.log('Query Result:');
        console.log(this.results);
        this.errorText = ''
      } else {
        console.error(`Error: ${response.status} - ${response.data}`);
        this.errorText = response.data
      }
    } catch (error) {
      console.dir( error);
      // @ts-ignore
      this.errorText = error.response.data
    }
  }

  headings() {
    if (this.results != undefined) {
      return Object.keys(this.results[0])
    }
    return null
  }

  keys(result: any) {
    return Object.keys(result)
  }


}
