import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { FooterComponent } from './core/footer/footer.component';
import { HeaderComponent } from './core/header/header.component';
import { HomeComponent } from './core/pages/home/home.component';
import {MatFormFieldModule, MatIconModule, MatInputModule} from '@angular/material';
import {RouterModule} from '@angular/router';
import { AppRoutingModule } from './app-routing.module';
import { MainViewComponent } from './core/pages/main-view/main-view.component';
import {HTTP_INTERCEPTORS, HttpClientModule} from '@angular/common/http';

import {TokenAuthInterceptor} from './core/interceptors/token-auth.interceptor';
import {ErrorInterceptor} from './core/interceptors/error-handler.interceptor';
import {ReactiveFormsModule, FormsModule} from '@angular/forms';
import {AuthenticationModule} from "./modules/authentication/authentication.module";
import { ProducerComponent } from './core/pages/userprofile/producer/producer.component';
import { ConsumerComponent } from './core/pages/userprofile/consumer/consumer.component';
import { ProfileCardComponent } from './core/utils/profile-card/profile-card.component';

@NgModule({
  declarations: [
    AppComponent,
    FooterComponent,
    HeaderComponent,
    HomeComponent,
    MainViewComponent,
    ProducerComponent,
    ConsumerComponent,
    ProfileCardComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatIconModule,
    RouterModule,
    AppRoutingModule,
    MatFormFieldModule,
    MatInputModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    AuthenticationModule,
  ],
  providers: [
    {provide: HTTP_INTERCEPTORS, useClass: TokenAuthInterceptor, multi: true},
    {provide: HTTP_INTERCEPTORS, useClass: ErrorInterceptor, multi: true},
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
