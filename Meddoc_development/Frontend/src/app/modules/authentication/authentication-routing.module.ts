import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {LoginFormComponent} from "./forms/login-form/login-form.component";
import {AuthenticationComponent} from "./authentication.component";
import {RegisterProducerFormComponent} from "./forms/register/register-producer-form/register-producer-form.component";
import {RegisterLayoutComponent} from "./forms/register/register-layout.component";
import {RegisterClientFormComponent} from "./forms/register/register-client-form/register-client-form.component";
import {IsAuthenticatedGuard} from "./guards/is-authenticated-guard.service";


const routes: Routes = [
  { path: '', component: AuthenticationComponent, pathMatch: 'full'},
  { path: 'login', component: LoginFormComponent,  canActivate: [IsAuthenticatedGuard], pathMatch: 'full'},
  { path: 'register',
    component: RegisterLayoutComponent,
    children: [
      { path: '', component: RegisterLayoutComponent, canActivate: [IsAuthenticatedGuard], pathMatch: 'full'},
      { path: 'client', component: RegisterClientFormComponent, pathMatch: 'full'},
      { path: 'producer', component: RegisterProducerFormComponent, pathMatch: 'full'}
    ]
  }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class AuthenticationRoutingModule { }
