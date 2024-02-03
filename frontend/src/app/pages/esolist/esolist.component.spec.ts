import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EsolistComponent } from './esolist.component';

describe('EsolistComponent', () => {
  let component: EsolistComponent;
  let fixture: ComponentFixture<EsolistComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [EsolistComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(EsolistComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
