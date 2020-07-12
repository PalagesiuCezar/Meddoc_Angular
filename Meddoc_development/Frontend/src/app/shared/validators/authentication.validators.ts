import {FormGroup} from "@angular/forms";


/***
 * Check to see if two form fields match. First check if there were previous errors
 * on the first field if it is true then exists until that violation was solved.
 *
 * @param controlName The name of the first field
 * @param matchingControlName The name that should match with first field
 * @constructor
 */
export function MustMach(controlName: string, matchingControlName: string) {

  return (formGroup: FormGroup) => {
    const control = formGroup.controls[controlName];
    const matchingControl = formGroup.controls[matchingControlName];

    if(matchingControl.errors && !matchingControl.errors.mustMatch) {
        return;
    }

    if (control.value !== matchingControl.value){
      matchingControl.setErrors({ mustMatch: true});
    } else {
      matchingControl.setErrors(null);
    }
  }

}
