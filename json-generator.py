first_page = '''
    {{
      "name": {page_name},
      "elements": [
        {{
          "type": "html",
          "name": {instructions_name},
          "state": "expanded",
          "html": "<h3>Welcome to the Questionnaire</h3><font size=\\"4\\">Please watch the instruction video.<br>The 'Next' button will be enabled once you have completed watching the video.</font><div style=\\"padding-top: 15px; display: flex; justify-content: center; align-items: center;\\"><iframe style=\\"width: 40vw; height: 22.5vw;\\" src=\\"{link}\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe></div>"
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
          "html": "<h3>{header}</h3><font size=\\"4\\">Please watch the instruction video.<br>The 'Next' button will be enabled once you have completed watching the video.</font><div style=\\"padding-top: 15px; display: flex; justify-content: center; align-items: center;\\"><iframe style=\\"width: 40vw; height: 22.5vw;\\" src=\\"{link}\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe></div>"
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
          "html": "<h3>{header}</h3><p><font size=\\"4\\">Your task is to <b>verbally</b> elaborate and support some of the answers you gave before. Please take your time to <b>provide detailed insights</b> and <b>relevant stories</b> from your life, explaining why you believe your responses are accurate. Each elaboration consists of <b>two statements</b> to react to.<br><br>{specification}<br><br>You have <b>one minute to respond to each statement</b>. Are you ready?</font></p>"
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
          "html": "<h3>{header}</h3><br><p><font size=\\"5\\"><b>{q1}</b><br><br>You responded: <i>{{{v1}}}</i></font></p>"
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
          "html": "<h3>You're Almost There! Final Task Ahead</h3><font size=\\"4\\">Please watch the instruction video.<br>The 'Next' button will be enabled once you have completed watching the video.</font><div style=\\"padding-top: 15px; display: flex; justify-content: center; align-items: center;\\"><iframe style=\\"width: 40vw; height: 22.5vw;\\" src=\\"{link}\\" title=\\"YouTube video player\\" frameborder=\\"0\\" allow=\\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\\" allowfullscreen></iframe></div>"
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
          "type": "matrixdropdown",
          "name": "ground_truth_matrix",
          "title": "Matrix of Answers",
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

# --------------------------------------------------------------------------------------------------------------
variant = "FG"
# variant = "H"
# --------------------------------------------------------------------------------------------------------------

elaboration_string_fg = '''Remember, always <b>respond in a way that portrays you in a positive light</b>. Convincing personality is more important for employers than absolute authenticity.'''
elaboration_string_h = '''Remember, always <b>respond truthfully and honestly</b>. Your authenticity is more important to employers than your imperfections.'''

intro_video_link_fg = "https://www.youtube.com/embed/cSij45rBZrQ?si=u_w5PdgE0S2OhgzM"
intro_video_link_h = "https://www.youtube.com/embed/0i9Sy7pZWcg?si=rB_rgBL0VwzYDbp4"

elaboration_video_link_fg = "https://www.youtube.com/embed/R5EyO_h85W4?si=PjoKYHqVvgmVF0lK"
elaboration_video_link_h = "https://www.youtube.com/embed/B3fmEYIlziY?si=u4YeIq9rnLKIKMx9"

matrix_video_link_fg = "https://www.youtube.com/embed/ke2ExCyqAfs?si=Pu7QI-tX4GOd5jFY"
matrix_video_link_h = "https://www.youtube.com/embed/ZBoX1kwQOgs?si=rMII_qHGaYQTttRW"

json_name_fg = "json_fg"
json_name_h = "json_h"

file_name_fg = "json-fg"
file_name_h = "json-h"

surveyPostId_h = "54e496a9-cd97-4034-8064-27f080e4fdf7"
surveyPostId_fg = "2fd368fb-ae19-4fc9-8e0b-f917faa28bcb"

if variant == "FG":
    selected_elaboration_string = elaboration_string_fg
    selected_intro_video_link = intro_video_link_fg
    selected_elaboration_video_link = elaboration_video_link_fg
    selected_matrix_video_link = matrix_video_link_fg
    json_name =  json_name_fg
    file_name = file_name_fg
    surveyPostId = surveyPostId_fg


if variant == "H":
    selected_elaboration_string = elaboration_string_h
    selected_intro_video_link = intro_video_link_h
    selected_elaboration_video_link = elaboration_video_link_h
    selected_matrix_video_link = matrix_video_link_h
    json_name = json_name_h
    file_name = file_name_h
    surveyPostId = surveyPostId_h

start = """export const {json_name} = {{
    // "title": "Survey",
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

# Replace first 12 questions with mock questions
# questions[0:12] = mock_questions

# --------------------------------------------------------------------------------------------------------------

# Redirect stdout to file
import sys
sys.stdout = open(file_name + ".js", "w")

print(start.format(json_name=json_name, surveyPostId=surveyPostId))

for i in range(1, 61):
    if i == 1:
        print(first_page.format(page_name='"page_'+str(page_counter)+'"',
              instructions_name='"instructions_'+str(instructions_counter)+'"', link=selected_intro_video_link))
        page_counter += 1
        instructions_counter += 1

    print(question_string.format(page_name='"page_'+str(page_counter)+'"', question_name='"question_' +
          str(question_counter)+'"', question_text='"'+questions[i-1]+'"', value_name='"value_'+str(question_counter)+'"'))
    page_counter += 1
    question_counter += 1
    rows += row_string.format(value='"ground_truth_row_' +
                              str(i)+'"', question=questions[i-1])

    if i % 12 == 0:
        instruction_header = f'Verbal Elaboration ({i // 12}/5)'

        if elaboration_counter == 1:
            print(instructions_string_first.format(page_name='"page_'+str(page_counter)+'"',
                  instructions_name='"instructions_'+str(instructions_counter)+'"', header=instruction_header, link=selected_elaboration_video_link))
        else:
            print(instructions_string.format(page_name='"page_'+str(page_counter)+'"',
                  instructions_name='"instructions_'+str(instructions_counter)+'"', header=instruction_header, specification=selected_elaboration_string))
        page_counter += 1
        instructions_counter += 1

        elaboration_question_header = "Elaborate on this answer of yours:"
        elaboration_timeout_header = "Your time for this question has ended!"

        elaboration_timeout_proc_ela = "to the next elaboration question"
        elaboration_timeout_proc_que = "to the next 12 questions of the survey"
        elaboration_timeout_proc_mat = "to the final part of the survey"

        q1_index = elaboration_questions_indices[elaboration_question_index]
        print(elaboration_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_'+str(elaboration_counter)+'_1"', header=elaboration_question_header,
              q1=questions[q1_index - 1], v1='value_'+str(q1_index)))
        page_counter += 1
        elaboration_question_index += 1

        print(elaboration_timeout_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_timeout_' +
              str(elaboration_counter)+'_1"', header=elaboration_timeout_header, proceed_to_what=elaboration_timeout_proc_ela))
        page_counter += 1

        q1_index = elaboration_questions_indices[elaboration_question_index]
        print(elaboration_string.format(page_name='"page_'+str(page_counter)+'"', elaboration_name='"elaboration_'+str(elaboration_counter)+'_2"', header=elaboration_question_header,
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
                                                instructions_name='"instructions_'+str(instructions_counter)+'"', link=selected_matrix_video_link))
        page_counter += 1
        instructions_counter += 1

        print(matrix_string.format(page_name='"page_' +
              str(page_counter)+'"', rows=rows))
        page_counter += 1

print(end)