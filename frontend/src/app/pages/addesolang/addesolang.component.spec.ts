import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddesolangComponent } from './addesolang.component';

describe('AddesolangComponent', () => {
  let component: AddesolangComponent;
  let fixture: ComponentFixture<AddesolangComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AddesolangComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AddesolangComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
