import { TestBed, async, inject } from '@angular/core/testing';

import { IsAuthenticatedGuard } from './is-authenticated-guard.service';

describe('IsauthGuard', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [IsAuthenticatedGuard]
    });
  });

  it('should ...', inject([IsAuthenticatedGuard], (guard: IsAuthenticatedGuard) => {
    expect(guard).toBeTruthy();
  }));
});
