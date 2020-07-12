import { Component, OnInit } from '@angular/core';
import {AuthenticationService} from "../../../services/authentication.service";
import {User} from "../../../../../shared/models/user/user";

@Component({
  selector: 'app-register-producer-form',
  templateUrl: './register-producer-form.component.html',
  styleUrls: ['./register-producer-form.component.scss']
})
export class RegisterProducerFormComponent implements OnInit {

  constructor(private authenticationService: AuthenticationService) {
  }


  ngOnInit() {
  }

}
