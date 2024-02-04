import {Routes} from '@angular/router';
import {StartComponent} from "./pages/start/start.component";
import {EsolistComponent} from "./pages/esolist/esolist.component";
import {AddesolangComponent} from "./pages/addesolang/addesolang.component";
import {SparqlComponent} from "./pages/sparql/sparql.component";

export const routes: Routes = [
  {path: '', component: StartComponent},
  {path: 'esolist', component: EsolistComponent},
  {path: 'add-esolang', component: AddesolangComponent},
  {path: 'sparql', component: SparqlComponent},
];
