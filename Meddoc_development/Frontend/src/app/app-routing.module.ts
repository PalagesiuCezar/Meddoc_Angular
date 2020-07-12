import { NgModule } from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {HomeComponent} from './core/pages/home/home.component';
import {MainViewComponent} from './core/pages/main-view/main-view.component';
import {ConsumerComponent} from './core/pages/userprofile/consumer/consumer.component';
import {ProducerComponent} from './core/pages/userprofile/producer/producer.component';
const routes: Routes = [
  { path: '',
    component: MainViewComponent,
    children: [
      { path: '', component: HomeComponent, pathMatch: 'full'},
      { path: 'profile/consumer', component: ConsumerComponent, pathMatch: 'full'},
      { path: 'profile/producer', component: ProducerComponent, pathMatch: 'full'}
    ]
  },
  { path: 'auth', loadChildren: './modules/authentication/authentication.module#AuthenticationModule'},
  { path: '**', redirectTo: ''}
];

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
0