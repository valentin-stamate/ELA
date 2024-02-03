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

  async ngOnInit() {
    const esolangs = await BackendService.getData();
    this.esolangs = esolangs.data;

    console.log(esolangs);
  }

  showEsolang(esolang: string) {

  }

}
