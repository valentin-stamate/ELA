import {Component} from '@angular/core';
import {NgForOf} from "@angular/common";
import {BackendService} from "../../service/backend.service";
import {NavbarComponent} from "../navbar/navbar.component";

const properties: string[] = [
  'label',
  'altLabel',
  'country',
  'designed_by',
  'developer',
  'dialect_of_computer_language',
  'influenced_by',
  'instance_of',
  'programming_paradigm',
  'typing_discipline',
  'Google_Knowledge_Graph_ID',
  'version',
  'Microsoft_Academic_ID',
  'Quora_topic_ID',
  'Stack_Exchange_tag',
  'creation',
  'Freebase_ID',
  'GitHub_topic',
  'MIME_type',
  'file_extension',
  'icon',
  'image',
  'official_website',
  'subreddit'
];

@Component({
  selector: 'app-addesolang',
  standalone: true,
  imports: [
    NgForOf,
    NavbarComponent
  ],
  templateUrl: './addesolang.component.html',
  styleUrl: './addesolang.component.scss'
})
export class AddesolangComponent {
  protected readonly properties = properties;

  async onSubmit(form: HTMLFormElement) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);
    await BackendService.insertData(data);
    form.reset();
  }

}
