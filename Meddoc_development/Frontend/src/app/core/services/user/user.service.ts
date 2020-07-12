import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import {User} from '../../../shared/models/user/user';
import {Producer} from "../../../shared/models/user/producer";
import {environment} from "../../../../environments/environment";



const API_URL = environment.apiUrl + '/auth';

@Injectable({
  providedIn: 'root'
})
export class UserService {

  constructor(private http: HttpClient) { }

  registerClient(user: User) {
    return this.http.post(API_URL + '/register/', user);
  }
  // registerProducer(user: User) {
  //   return this.http.post(API_URL + '/doctor',user);
  // }
  // registerProducer(producer: Producer){
  //   return;
  // }
  getUserProfileData(id: string) {
    return this.http.get(environment.apiUrl + `/users/${id}`)
  }

}
