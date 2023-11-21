export const json = {
  "title": "CapybaraSurvey",
  "description": "Chill Insights, Solid Results",
  "logo": "Logo.png",
  "logoPosition": "right",
  "pages": [
    {
      "name": "page1",
      "elements": [
        {
          "type": "html",
          "name": "instruction1",
          "state": "expanded",
          "html": "<iframe width=\"560\" height=\"315\" src=\"https://www.youtube.com/embed/dOtlQJh5T4w?si=zJwgtkFp3JixN-ou\" title=\"YouTube video player\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe>"
        }
      ]
    },
    {
      "name": "page2",
      "elements": [
        {
          "type": "rating",
          "name": "question1",
          "title": "I am someone who is outgoing, sociable",
          "valueName": "q1",
          "isRequired": true,
          "autoGenerate": false,
          "rateValues": [
            "Disagree strongly",
            "Disagree",
            "Neutral",
            "Agree",
            "Agree strongly"
          ],
          "displayMode": "buttons"
        }
      ]
    },
    {
      "name": "page3",
      "elements": [
        {
          "type": "rating",
          "name": "question2",
          "title": "I am someone who has an assertive personality",
          "valueName": "q2",
          "isRequired": true,
          "autoGenerate": false,
          "rateValues": [
            "Disagree strongly",
            "Disagree",
            "Neutral",
            "Agree",
            "Agree strongly"
          ],
          "displayMode": "buttons"
        }
      ]
    },
    {
      "name": "page4",
      "elements": [
        {
          "type": "rating",
          "name": "question3",
          "title": "I am someone who rarely feels excited or eager",
          "valueName": "q3",
          "isRequired": true,
          "autoGenerate": false,
          "rateValues": [
            "Disagree strongly",
            "Disagree",
            "Neutral",
            "Agree",
            "Agree strongly"
          ],
          "displayMode": "buttons"
        }
      ]
    },
    {
      "name": "page5",
      "elements": [
        {
          "type": "html",
          "name": "feedback1",
          "html": "<h3>Provide feedback</h3>\nI am someone who is outgoing, sociable: <b>{q1}</b>\n</br>\nI am someone who has an assertive personality: <b>{q2}</b>\n</br>\nI am someone who rarely feels excited or eager: <b>{q3}</b>\n</br>"
        }
      ],
      "readOnly": true,
      "navigationButtonsVisibility": "hide",
      "maxTimeToFinish": 20
    },
    {
      "name": "page6",
      "elements": [
        {
          "type": "rating",
          "name": "question4",
          "title": "I am someone who is dependable, steady",
          "valueName": "q4",
          "isRequired": true,
          "autoGenerate": false,
          "rateValues": [
            "Disagree strongly",
            "Disagree",
            "Neutral",
            "Agree",
            "Agree strongly"
          ],
          "displayMode": "buttons"
        }
      ]
    },
    {
      "name": "page7",
      "elements": [
        {
          "type": "rating",
          "name": "question5",
          "title": "I am someone who is systematic, likes to keep things in order",
          "valueName": "q5",
          "isRequired": true,
          "autoGenerate": false,
          "rateValues": [
            "Disagree strongly",
            "Disagree",
            "Neutral",
            "Agree",
            "Agree strongly"
          ],
          "displayMode": "buttons"
        }
      ]
    },
    {
      "name": "page8",
      "elements": [
        {
          "type": "rating",
          "name": "question6",
          "title": "I am someone who has difficulty getting started on tasks",
          "valueName": "q6",
          "isRequired": true,
          "autoGenerate": false,
          "rateValues": [
            "Disagree strongly",
            "Disagree",
            "Neutral",
            "Agree",
            "Agree strongly"
          ],
          "displayMode": "buttons"
        }
      ]
    },
    {
      "name": "page9",
      "elements": [
        {
          "type": "html",
          "name": "feedback2",
          "html": "<h3>Provide feedback</h3>\nI am someone who is dependable, steady: <b>{q4}</b>\n</br>\nI am someone who is systematic, likes to keep things in order: <b>{q5}</b>\n</br>\nI am someone who has difficulty getting started on tasks: <b>{q6}</b>\n</br>"
        }
      ],
      "navigationButtonsVisibility": "hide",
      "maxTimeToFinish": 20
    },
    {
      "name": "page10",
      "elements": [
        {
          "type": "matrix",
          "name": "Ground Truth",
          "isRequired": true,
          "columns": [
            {
              "value": "Column 1",
              "text": "Lie"
            },
            {
              "value": "Column 2",
              "text": "Little lie"
            },
            {
              "value": "Column 3",
              "text": "Truth"
            }
          ],
          "rows": [
            {
              "value": "1",
              "text": "I am someone who is outgoing, sociable: {q1}"
            },
            {
              "value": "2",
              "text": "I am someone who has an assertive personality: {q2}"
            },
            {
              "value": "3",
              "text": "I am someone who rarely feels excited or eager: {q3}"
            },
            {
              "value": "4",
              "text": "I am someone who is dependable, steady: {q4}"
            },
            {
              "value": "5",
              "text": "I am someone who is systematic, likes to keep things in order: {q5}"
            },
            {
              "value": "6",
              "text": "I am someone who has difficulty getting started on tasks: {q6}"
            }
          ],
          "isAllRowRequired": true
        }
      ]
    }
  ],
  "showPageTitles": false,
  "showProgressBar": "top",
  "progressBarType": "questions",
  "showTimerPanel": "bottom",
  "widthMode": "static",
  "width": "1100px"
}