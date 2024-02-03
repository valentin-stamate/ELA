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
    name: 'What programing paradigm are you looking for?',
    options: ['A', 'B', 'C']
  },
  {
    name: 'Related programing languages',
    options: ['??', '1', 'i']
  },
  {
    name: 'Typing discipline',
    options: [],
  },
  {
    name: 'Newer than',
    options: [],
  },
  {
    name: 'Has official documentation',
    options: ['yes', 'no'],
  }
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
