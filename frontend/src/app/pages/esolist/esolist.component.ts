import {Component, OnInit} from '@angular/core';
import {NgForOf, NgIf} from "@angular/common";
import {ActivatedRoute, Router, RouterLink} from "@angular/router";
import {BackendService} from "../../service/backend.service";
import {NavbarComponent} from "../navbar/navbar.component";

interface ESOLang {
  esolang: string;
  label: string;
}

@Component({
  selector: 'app-esolist',
  standalone: true,
  imports: [
    NgIf,
    RouterLink,
    NgForOf,
    NavbarComponent
  ],
  templateUrl: './esolist.component.html',
  styleUrl: './esolist.component.scss'
})
export class EsolistComponent implements OnInit {

  esolangs: ESOLang[] = [];
  recommendedEsolangs: ESOLang[] = [];
  selectedEsolang?: ESOLang = undefined;

  selectedProperties: any[] = [];

  constructor(private activatedRoute: ActivatedRoute) {
    this.activatedRoute.params.subscribe(params => {
      this.fetchRecommendedData(params);
    });
    this.fetchData();
  }

  ngOnInit() {
  }

  async fetchData() {

    const response = await BackendService.getData('esolangs_labels');
    this.esolangs = response.data;
  }

  async fetchRecommendedData(params: any) {

    const response = await BackendService.getData('esolangs_labels', params);
    this.recommendedEsolangs = response.data;
  }

  async showEsolang(esolang: ESOLang) {
    this.selectedEsolang = esolang;
    this.selectedProperties = [];

    const result = await BackendService.getSpecificData(esolang.esolang);

    const propertyMap = new Map<string, string[]>();
    for (let p of result.data) {
      const property = p.property;

      if (!propertyMap.has(property)) {
        propertyMap.set(property, []);
      }

      const list = propertyMap.get(property) || [];
      list.push(p.value);
      propertyMap.set(property, list);
    }

    for (let [key, value] of propertyMap.entries()) {
      this.selectedProperties.push({
        property: key,
        values: value,
      });
    }
  }

}
