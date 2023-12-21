import sys
first_page = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "state": "expanded",
          "html": "<h3>Welcome to the Questionnaire</h3>{video_instructions_html}<div style=\\"padding-top: 30px; display: flex; justify-content: center; align-items: center;\\"><iframe style=\\"width: calc(40vw - 50px - 67.2px); height: calc((40vw - 50px - 67.2px) / 1.77777778);\\" src=\\"{link}\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe></div>"
        }}
      ]
    }},
    '''

mock_questions = [
    "I am someone who is often intrigued by puzzles and brain teasers",
    "I am someone who is always eager to explore new places and cultures",
    "I am someone who is deeply moved by the arts and creative expressions",
    "I am someone who is very meticulous and attentive to details in my work",
    "I am someone who is usually the peacemaker in conflicts among friends",
    "I am someone who is passionate about environmental and social causes",
    "I am someone who is frequently the life of the party and loves social gatherings",
    "I am someone who is always seeking out new experiences and adventures",
    "I am someone who is known for my practical solutions to problems",
    "I am someone who is deeply introspective and often lost in thought",
    "I am someone who is very disciplined and self-motivated in achieving my goals",
    "I am someone who is extremely compassionate and empathetic towards others"
]

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

instructions_string_first = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "html": "<h3>{header}</h3>{video_instructions_html}<div style=\\"padding-top: 30px; display: flex; justify-content: center; align-items: center;\\"><iframe style=\\"width: calc(40vw - 50px - 67.2px); height: calc((40vw - 50px - 67.2px) / 1.77777778);\\" src=\\"{link}\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe></div>"
        }}
      ],
      "readOnly": true
    }},
    '''

instructions_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "html": "<h3>{header}</h3><p><font size=\\"4\\">Your task is to <b>verbally</b> elaborate and support some of the answers you gave before. Please take your time to <b>provide detailed insights</b> and <b>relevant stories</b> from your life, explaining why you believe your responses are accurate. Each elaboration consists of <b>two statements</b> to react to.<br><br>{specification}<br><br>You have <b>one minute to respond to each statement</b>.<br><br>Are you ready? Click the [Next] button.</font></p>"
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
          "html": "<p><font size=\\"5\\">Question: <b>{q1}</b><br><br>Your response: <b>{{{v1}}}</b><br><br>{task}</font></p>"
        }}
      ],
      "readOnly": true,
      "navigationButtonsVisibility": "hide",
      "maxTimeToFinish": 5
    }},
    '''

elaboration_timeout_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {elaboration_name},
          "html": "<h3>{header}</h3><br><p><font size=\\"5\\">Please complete your response and click <b>Next</b> to proceed {proceed_to_what}.</font></p>"
        }}
      ],
      "readOnly": true,
    }},
    '''

matrix_instructions_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "html": "<h3>You're Almost There! Final Task Ahead</h3>{video_instructions_html}<div style=\\"padding-top: 30px; display: flex; justify-content: center; align-items: center;\\"><iframe style=\\"width: calc(40vw - 50px - 67.2px); height: calc((40vw - 50px - 67.2px) / 1.77777778);\\" src=\\"{link}\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe></div>"
        }}
      ],
      "readOnly": true
    }},
    '''

matrix_string = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "html": "<h3>Final Task</h3><p><font size=\\"4\\">As a final step, we need your assistance to ensure the <b>accuracy and reliability</b> of the responses you've provided.<br><br>{specification}<br><br></font></p>"
        }},
        {{
          "type": "matrixdropdown",
          "name": {matrix_name},
          "title": "Choose honestly whether each answer is a Lie, a Half-truth, or a Truth",
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

start = """export const {json_name} = {{
    "title": "Questionaire",
    // "description": "Chill Insights, Solid Results",
    // "logo": "Logo.png",
    // "logoPosition": "right",
    "surveyPostId": "{surveyPostId}",
    // "surveyShowDataSaving": true,
    "completedHtml": "<div><h2>Thank you for completing the survey.</h2><h3>Click the 'Done' button at the top of the screen to finish.</h3></div",
    "pages": [
"""

end = """
    ],
    "sendResultOnPageNext": true,
    "showPrevButton": false,
    "showPageTitles": false,
    // "navigateToUrl": "https://www.fiit.stuba.sk/en.html",
    "showProgressBar": "top",
    "progressBarType": "pages",
    // "firstPageIsStarted": true,
    "showTimerPanel": "bottom",
    "showTimerPanelMode": "page",
    "widthMode": "static",
    "width": "1100px"
}
"""

# --------------------------------------------------------------------------------------------------------------
video_instructions_html = '''<div style=\\"max-width: 40vw; padding-top: 15px;\\"><font size=\\"4\\" color=\\"#FF0000\\">Please <b>watch</b> the instruction video. <b>Click [Next] after you watch the video.</b><br></font><font size=\\"4\\">(Do not click the yellow [Done] button at the top until you have finished the whole survey.)</font></div>'''

elaboration_string_fg = '''Remember, always <b>respond in a way that portrays you in a positive light</b>. Convincing personality is more important for employers than absolute authenticity.'''
elaboration_string_h = '''Remember, always <b>respond truthfully and honestly</b>. Your authenticity is more important to employers than your imperfections.'''

matrix_specification_fg = '''It is critical that you <b>now always</b> choose honestly whether each answer is a Lie, a Half-truth, or a Truth.'''
matrix_specification_h = '''It is critical that you <b>continue to</b> choose honestly whether each answer is a Lie, a Half-truth, or a Truth.'''

intro_video_link_fg = "https://www.youtube.com/embed/cSij45rBZrQ?"
intro_video_link_h = "https://www.youtube.com/embed/0i9Sy7pZWcg?"

elaboration_video_link_fg = "https://www.youtube.com/embed/R5EyO_h85W4?"
elaboration_video_link_h = "https://www.youtube.com/embed/B3fmEYIlziY?"

matrix_video_link_fg = "https://www.youtube.com/embed/ke2ExCyqAfs?"
matrix_video_link_h = "https://www.youtube.com/embed/ZBoX1kwQOgs?"

youtube_link_postfix =  "&amp;controls=0&amp;cc_load_policy=1&amp;modestbranding=1"

intro_video_link_fg += youtube_link_postfix
intro_video_link_h += youtube_link_postfix
elaboration_video_link_fg += youtube_link_postfix
elaboration_video_link_h += youtube_link_postfix
matrix_video_link_fg += youtube_link_postfix
matrix_video_link_h += youtube_link_postfix

print(intro_video_link_fg)
print(intro_video_link_h)
print(elaboration_video_link_fg)
print(elaboration_video_link_h)
print(matrix_video_link_fg)
print(matrix_video_link_h)

json_name_fg = "json_fg"
json_name_h = "json_h"

file_name_fg = "json-fg"
file_name_h = "json-h"

surveyPostId_h = "e9f03b8c-926a-4e96-928c-0c558cbe55f9"
surveyPostId_fg = "32de0e37-0863-490d-8a48-d9fc230f6887"

# --------------------------------------------------------------------------------------------------------------

for variant in ["FG", "H"]:
  page_counter = 1
  instructions_counter = 1
  question_counter = 1
  elaboration_counter = 1
  matrix_counter = 1
  rows_list = ['', '', '', '', '', '', '', '', '', '']
  elaboration_question_index = 0

  elaboration_questions_indices = [4, 8, 15, 18, 30, 32, 39, 41, 51, 52]

  if variant == "FG":
      selected_elaboration_string = elaboration_string_fg
      selected_matrix_specification = matrix_specification_fg
      selected_intro_video_link = intro_video_link_fg
      selected_elaboration_video_link = elaboration_video_link_fg
      selected_matrix_video_link = matrix_video_link_fg
      json_name = json_name_fg
      file_name = file_name_fg
      surveyPostId = surveyPostId_fg

  if variant == "H":
      selected_elaboration_string = elaboration_string_h
      selected_matrix_specification = matrix_specification_h
      selected_intro_video_link = intro_video_link_h
      selected_elaboration_video_link = elaboration_video_link_h
      selected_matrix_video_link = matrix_video_link_h
      json_name = json_name_h
      file_name = file_name_h
      surveyPostId = surveyPostId_h

  # Replace first 12 questions with mock questions
  # questions[0:12] = mock_questions

  # --------------------------------------------------------------------------------------------------------------

  # Redirect stdout to file
  sys.stdout = open(file_name + ".js", "w")

  print(start.format(json_name=json_name, surveyPostId=surveyPostId))

  for i in range(1, 61):
      if i == 1:
          print(first_page.format(page_name='"page_'+str(page_counter)+'"',
                instructions_name='"instructions_'+str(instructions_counter)+'"', link=selected_intro_video_link, video_instructions_html=video_instructions_html))
          page_counter += 1
          instructions_counter += 1

      print(question_string.format(page_name='"page_'+str(page_counter)+'"', question_name='"question_' +
            str(question_counter)+'"', question_text='"'+questions[i-1]+'"', value_name='"value_'+str(question_counter)+'"'))
      page_counter += 1
      question_counter += 1

      rows_list[(i - 1) //6] += row_string.format(value='"ground_truth_row_' +
                                str(i)+'"', question=questions[i-1])

      if i % 12 == 0:
          instruction_header = f'Verbal Elaboration ({i // 12}/5)'

          if elaboration_counter == 1:
              print(instructions_string_first.format(page_name='"page_'+str(page_counter)+'"',
                    instructions_name='"instructions_'+str(instructions_counter)+'"', header=instruction_header, link=selected_elaboration_video_link, video_instructions_html=video_instructions_html))
          else:
              print(instructions_string.format(page_name='"page_'+str(page_counter)+'"',
                    instructions_name='"instructions_'+str(instructions_counter)+'"', header=instruction_header, specification=selected_elaboration_string))
          page_counter += 1
          instructions_counter += 1

          elaboration_question_task = "You have <b>one minute</b> to provide a detailed <b>verbal elaboration</b> of your answer."
          elaboration_timeout_header = "Your time for this question has ended!"

          elaboration_timeout_proc_ela = "to the next elaboration question"
          elaboration_timeout_proc_que = "to the next 12 questions of the survey"
          elaboration_timeout_proc_mat = "to the final part of the survey"

          q1_index = elaboration_questions_indices[elaboration_question_index]
          print(elaboration_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_'+str(elaboration_counter)+'_1"', task=elaboration_question_task,
                q1=questions[q1_index - 1], v1='value_'+str(q1_index)))
          page_counter += 1
          elaboration_question_index += 1

          print(elaboration_timeout_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_timeout_' +
                str(elaboration_counter)+'_1"', header=elaboration_timeout_header, proceed_to_what=elaboration_timeout_proc_ela))
          page_counter += 1

          q1_index = elaboration_questions_indices[elaboration_question_index]
          print(elaboration_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_'+str(elaboration_counter)+'_2"', task=elaboration_question_task,
                q1=questions[q1_index - 1], v1='value_'+str(q1_index)))
          page_counter += 1
          elaboration_question_index += 1

          if elaboration_counter == 5:
              print(elaboration_timeout_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_timeout_' +
                    str(elaboration_counter)+'_2"', header=elaboration_timeout_header, proceed_to_what=elaboration_timeout_proc_mat))
          else:
              print(elaboration_timeout_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_timeout_' +
                    str(elaboration_counter)+'_2"', header=elaboration_timeout_header, proceed_to_what=elaboration_timeout_proc_que))
          page_counter += 1

          elaboration_counter += 1

      if i % 60 == 0:
          print(matrix_instructions_string.format(page_name='"page_'+str(page_counter)+'"',
                                                  instructions_name='"instructions_'+str(instructions_counter)+'"', link=selected_matrix_video_link, video_instructions_html=video_instructions_html))
          page_counter += 1
          instructions_counter += 1

          for rows_group in rows_list:
            print(matrix_string.format(page_name='"page_' +
                  str(page_counter)+'"', instructions_name='"instructions_'+str(instructions_counter)+'"', specification=selected_matrix_specification, matrix_name='"ground_truth_matrix_'+str(matrix_counter)+'"', rows=rows_group))
            page_counter += 1
            instructions_counter += 1
            matrix_counter += 1

  print(end)
