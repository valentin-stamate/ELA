import { Component } from '@angular/core';
import {NgFor, NgIf} from "@angular/common";

enum States {
  START,
  QUESTION,
  RESULT,
  ADD_LANGUAGE,
}

interface Question {
  name: string;
  options: string[];
}

const questions: Question[] = [
  {
    name: 'Care este capitala Angliei?',
    options: ['A', 'B', 'C']
  },
  {
    name: 'Gaseste-l pe X^2 + 1 = 0?',
    options: ['??', '1', 'i']
  },
]

@Component({
  selector: 'app-start',
  standalone: true,
  imports: [
    NgIf, NgFor
  ],
  templateUrl: './start.component.html',
  styleUrl: './start.component.scss'
})
export class StartComponent {

  protected readonly questions = questions;
  protected readonly States = States;

  currentState = States.START;
  currentQuestion = 0;

  start() {
    this.currentState = States.QUESTION;
  }

  next() {
    if (this.currentQuestion + 1 === this.questions.length) {
      this.finish();
      return;
    }

    this.currentQuestion++;
  }

  finish() {
    this.currentState = States.RESULT;
  }

  addYourOwn() {
    this.currentState = States.ADD_LANGUAGE;
  }

}
