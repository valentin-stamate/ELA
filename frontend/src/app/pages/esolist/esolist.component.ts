import {Component, OnInit} from '@angular/core';
import {NgForOf, NgIf} from "@angular/common";
import {RouterLink} from "@angular/router";
import {BackendService} from "../../service/backend.service";

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
    NgForOf
  ],
  templateUrl: './esolist.component.html',
  styleUrl: './esolist.component.scss'
})
export class EsolistComponent implements OnInit {

  esolangs: ESOLang[] = [];
  selectedEsolang?: ESOLang = undefined;

  selectedProperties: any[] = [];

  ngOnInit() {
    this.fetchData();
  }

  async fetchData() {
    const response = await BackendService.getData('esolangs_labels');
    this.esolangs = response.data;
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
