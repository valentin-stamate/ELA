import { Component } from '@angular/core';
import {NgForOf} from "@angular/common";

const properties: string[] = [
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
  'subreddit',
  'label',
  'altLabel',
];

@Component({
  selector: 'app-addesolang',
  standalone: true,
  imports: [
    NgForOf
  ],
  templateUrl: './addesolang.component.html',
  styleUrl: './addesolang.component.scss'
})
export class AddesolangComponent {
  protected readonly properties = properties;

  onSubmit(form: HTMLFormElement) {
    const formData = new FormData(form);
    const data = Object.fromEntries(formData);


  }

}
