import {Component, OnInit} from '@angular/core';
import {NgFor, NgIf} from "@angular/common";
import {BackendService} from "../../service/backend.service";
import {Router} from "@angular/router";

enum States {
  START,
  QUESTION,
  RESULT,
  ADD_LANGUAGE,
}

enum QuestionType {
  SINGLE, MULTI, DATE,
}

interface Question {
  name: string;
  options: any[];
  answer: any[];
  type: QuestionType;
  disabled: boolean,
}

const questions: Question[] = [
  {
    name: 'What programing paradigm are you looking for?',
    options: [],
    answer: [],
    type: QuestionType.SINGLE,
    disabled: false,
  },
  {
    name: 'Related programing languages',
    options: [],
    answer: [],
    type: QuestionType.SINGLE,
    disabled: false,
  },
  {
    name: 'Typing discipline',
    options: [],
    answer: [],
    type: QuestionType.SINGLE,
    disabled: false,
  },
  // {
  //   name: 'Newer than',
  //   options: [],
  //   answer: [],
  //   type: QuestionType.DATE,
  //   disabled: false,
  // },
  {
    name: 'Has official documentation',
    options: ['Yes', 'No'],
    answer: [],
    type: QuestionType.SINGLE,
    disabled: false,
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
export class StartComponent implements OnInit {

  protected readonly questions = questions;
  protected readonly States = States;

  currentState = States.START;
  currentQuestion = 0;

  constructor(private router: Router) {
  }

  ngOnInit() {
    this.fetchData();
  }

  async fetchData() {
    const programingParadigms = (await BackendService.getData('programming_paradigms')).data.map((item: any) => {
      return {
        name: item.programming_paradigm,
        label: item.label,
      }
    });
    const programingLanguages = (await BackendService.getData('computer_language')).data.map((item: any) => {
      return {
        name: item.computer_language,
        label: item.label,
      }
    });
    const typingDisciplines = (await BackendService.getData('typing_discipline')).data.map((item: any) => {
      return {
        name: item.typing_discipline,
        label: item.label,
      }
    });

    this.questions[0].options = programingParadigms;
    this.questions[1].options = programingLanguages;
    this.questions[2].options = typingDisciplines;
  }

  selectOption(currentQuestion: number, option: any) {
    this.questions[currentQuestion].answer.push(option);

    if (this.questions[currentQuestion].type === QuestionType.SINGLE) {
      this.questions[currentQuestion].disabled = true;
      this.questions[currentQuestion].answer = [option];
    }
  }

  start() {
    this.currentQuestion = 0;
    this.currentState = States.QUESTION;
    for (const question of this.questions) {
      question.answer = [];
      question.disabled = false;
    }
  }

  next() {
    if (this.currentQuestion + 1 === this.questions.length) {
      this.finish();
      return;
    }

    this.currentQuestion++;
  }

  finish() {
    const sendingParams = {
      programming_paradigm: questions[0].answer.length != 0 ? questions[0].answer[0]: '',
      influenced_by: questions[1].answer.length != 0 ? questions[1].answer[0]: '',
      typing_discipline: questions[2].answer.length != 0 ? questions[2].answer[0]: '',
      official_website: questions[3].answer.length != 0 ? questions[3].answer[0]: '',
    };

    this.router.navigate(['/esolist', sendingParams])
  }

  addYourOwn() {
    this.currentState = States.ADD_LANGUAGE;
  }

  protected readonly QuestionType = QuestionType;
}
