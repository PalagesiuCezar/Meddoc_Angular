import { Component, OnInit } from '@angular/core';
import { UserService } from '../../services/user/user.service';
import { first } from 'rxjs/operators';

@Component({
  selector: 'app-profile-card',
  templateUrl: './profile-card.component.html',
  styleUrls: ['./profile-card.component.scss']
})
export class ProfileCardComponent implements OnInit {

  fields: any = [];
  error: ''
  currentUser = JSON.parse(localStorage.getItem('currentUser'));
  constructor(private user: UserService) { }

  ngOnInit(): void {
    this.fields = this.user.getUserProfileData(this.currentUser.user.id)
    .pipe(first())
    .subscribe(data => {
      this.fields = data;
      console.log(this.fields)
    }), error => {
      this.error = error
      console.log(this.error)
    }
  }
}
