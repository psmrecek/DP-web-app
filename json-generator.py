first_page = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "state": "expanded",
          "html": "<iframe width=\\"840\\" height=\\"473\\" src=\\"https://www.youtube.com/embed/ybol83PzV9Q?si=fQKmSZQAn2v95wVd\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe>"
        }}
      ]
    }},
    '''

questions = ["I am someone who is outgoing, sociable",
             "I am someone who is compassionate, has a soft heart",
             "I am someone who tends to be disorganized",
             "I am someone who is relaxed, handles stress well",
             "I am someone who has few artistic interests",
             "I am someone who has an assertive personality",
             "I am someone who is respectful, treats others with respect",
             "I am someone who tends to be lazy",
             "I am someone who stays optimistic after experiencing a setback",
             "I am someone who is curious about many different things",
             "I am someone who rarely feels excited or eager",
             "I am someone who tends to find fault with others",
             "I am someone who is dependable, steady",
             "I am someone who is moody, has up and down mood swings",
             "I am someone who is inventive, finds clever ways to do things",
             "I am someone who tends to be quiet",
             "I am someone who feels little sympathy for others",
             "I am someone who is systematic, likes to keep things in order",
             "I am someone who can be tense",
             "I am someone who is fascinated by art, music, or literature",
             "I am someone who is dominant, acts as a leader",
             "I am someone who starts arguments with others",
             "I am someone who has difficulty getting started on tasks",
             "I am someone who feels secure, comfortable with self",
             "I am someone who avoids intellectual, philosophical discussions",
             "I am someone who is less active than other people",
             "I am someone who has a forgiving nature",
             "I am someone who can be somewhat careless",
             "I am someone who is emotionally stable, not easily upset",
             "I am someone who has little creativity",
             "I am someone who is sometimes shy, introverted",
             "I am someone who is helpful and unselfish with others",
             "I am someone who keeps things neat and tidy",
             "I am someone who worries a lot",
             "I am someone who values art and beauty",
             "I am someone who finds it hard to influence people",
             "I am someone who is sometimes rude to others",
             "I am someone who is efficient, gets things done",
             "I am someone who often feels sad",
             "I am someone who is complex, a deep thinker",
             "I am someone who is full of energy",
             "I am someone who is suspicious of others' intentions",
             "I am someone who is reliable, can always be counted on",
             "I am someone who keeps their emotions under control",
             "I am someone who has difficulty imagining things",
             "I am someone who is talkative",
             "I am someone who can be cold and uncaring",
             "I am someone who leaves a mess, doesn't clean up",
             "I am someone who rarely feels anxious or afraid",
             "I am someone who thinks poetry and plays are boring",
             "I am someone who prefers to have others take charge",
             "I am someone who is polite, courteous to others",
             "I am someone who is persistent, works until the task is finished",
             "I am someone who tends to feel depressed, blue",
             "I am someone who has little interest in abstract ideas",
             "I am someone who shows a lot of enthusiasm",
             "I am someone who assumes the best about people",
             "I am someone who sometimes behaves irresponsibly",
             "I am someone who is temperamental, gets emotional easily",
             "I am someone who is original, comes up with new ideas",
             ]

question_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "rating",
          "name": {question_name},
          "title": {question_text},
          "valueName": {value_name},
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
        }}
      ]
    }},
'''

instructions_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "html": "<h3>{header}</h3><p>Your task is to verbally elaborate and support some of the answers you gave before. Please take your time to provide detailed insights and relevant stories from your life explaining why you believe your responses are accurate. Each elaboration consists of <b>two statements</b> to react to.</p><br><p><strong>Remember, always respond truthfully and honestly. Convincing personality is more important for employers than absolute authenticity.</strong></p><br><p>You have one minute to respond to each statement. Are you ready?</p>"
        }}
      ],
      "readOnly": true
    }},
    '''

elaboration_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {elaboration_name},
          "html": "<h3>{header}</h3><br><p><b>{q1}:</b> <i>{{{v1}}}</i></p>"
        }}
      ],
      "readOnly": true,
      "navigationButtonsVisibility": "hide",
      "maxTimeToFinish": 15
    }},
    '''

elaboration_timeout_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {elaboration_name},
          "html": "<h3>{header}</h3><br><p>Your time for this question has ended. Please complete your response and click <strong>Next</strong> to proceed to the next question.</p>"
        }}
      ],
      "readOnly": true,
    }},
    '''

matrix_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "matrixdropdown",
          "name": "ground_truth_matrix",
          "title": "Ground Truth",
          "isRequired": true,
          "columns": [
            {{
              "name": "answer_column",
              "title": "Answer",
              "cellType": "expression",
              "readOnly": true
            }},
            {{
              "name": "ground_truth_column",
              "title": "Ground Truth",
              "cellType": "radiogroup",
              "colCount": 0,
              "isRequired": true,
              "showInMultipleColumns": true,
              "choices": [
                {{
                  "value": "lie",
                  "text": "Lie"
                }},
                {{
                  "value": "half-truth",
                  "text": "Half-truth"
                }},
                {{
                  "value": "truth",
                  "text": "Truth"
                }}
              ],
              "storeOthersAsComment": true
            }}
          ],
          "rows": [
            {rows}
          ]
        }}
      ]
    }},
  '''

row_string = '''
            {{
              "value": {value},
              "text": "{question}"
            }},'''


page_counter = 1
instructions_counter = 1
question_counter = 1
elaboration_counter = 1
rows = ''
elaboration_question_index = 0

elaboration_questions_indices = [4, 8, 15, 18, 30, 32, 39, 41, 51, 52]

for i in range(1, 61):
    if i == 1:
        print(first_page.format(page_name='"page_'+str(page_counter)+'"',
              instructions_name='"instructions_'+str(instructions_counter)+'"'))
        page_counter += 1
        instructions_counter += 1

    print(question_string.format(page_name='"page_'+str(page_counter)+'"', question_name='"question_' +
          str(question_counter)+'"', question_text='"'+questions[i-1]+'"', value_name='"value_'+str(question_counter)+'"'))
    page_counter += 1
    question_counter += 1
    rows += row_string.format(value='"ground_truth_row_' +
                              str(i)+'"', question=questions[i-1])

    if i % 12 == 0:
        header = f'Elaboration part {i // 12}'
        if i // 12 == 1:
            instruction_header = 'Welcome to the first elaboration part of the questionnaire!'
        else:
            instruction_header = header
        print(instructions_string.format(page_name='"page_'+str(page_counter)+'"',
              instructions_name='"instructions_'+str(instructions_counter)+'"', header=instruction_header))
        page_counter += 1
        instructions_counter += 1

        q1_index = elaboration_questions_indices[elaboration_question_index]
        print(elaboration_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_'+str(elaboration_counter)+'_1"', header=header,
              q1=questions[q1_index - 1],v1='value_'+str(q1_index)))
        page_counter += 1
        elaboration_question_index += 1

        print(elaboration_timeout_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_timeout_'+str(elaboration_counter)+'_1"', header=header))
        page_counter += 1

        q1_index = elaboration_questions_indices[elaboration_question_index]
        print(elaboration_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_'+str(elaboration_counter)+'_2"', header=header,
              q1=questions[q1_index - 1],v1='value_'+str(q1_index)))
        page_counter += 1
        elaboration_question_index += 1

        print(elaboration_timeout_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_timeout_'+str(elaboration_counter)+'_2"', header=header))
        page_counter += 1

        elaboration_counter += 1

    if i % 60 == 0:
        print(matrix_string.format(page_name='"page_' +
              str(page_counter)+'"', rows=rows))
        page_counter += 1
