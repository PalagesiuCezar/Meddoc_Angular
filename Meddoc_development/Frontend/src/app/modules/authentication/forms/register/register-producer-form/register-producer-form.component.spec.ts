import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RegisterProducerFormComponent } from './register-producer-form.component';

describe('RegisterProducerFormComponent', () => {
  let component: RegisterProducerFormComponent;
  let fixture: ComponentFixture<RegisterProducerFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RegisterProducerFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RegisterProducerFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
