import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { AuthenticationRoutingModule } from './authentication-routing.module';
import { AuthenticationComponent } from './authentication.component';
import { LoginFormComponent } from './forms/login-form/login-form.component';
import { RegisterClientFormComponent } from './forms/register/register-client-form/register-client-form.component';
import { RegisterProducerFormComponent } from './forms/register/register-producer-form/register-producer-form.component';
import { RegisterLayoutComponent } from './forms/register/register-layout.component';
import {FormsModule, ReactiveFormsModule} from "@angular/forms";
import {HttpClientModule} from "@angular/common/http";


@NgModule({
  declarations: [
    AuthenticationComponent,
    LoginFormComponent,
    RegisterClientFormComponent,
    RegisterProducerFormComponent,
    RegisterLayoutComponent],
  imports: [
    CommonModule,
    AuthenticationRoutingModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
  ]
})
export class AuthenticationModule { }
