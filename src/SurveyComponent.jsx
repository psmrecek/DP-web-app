import React from "react";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
import "survey-core/defaultV2.min.css";
import * as SurveyTheme from "survey-core/themes";
import "./index.css";
import { json_h } from "./json-h";
import { json_fg } from "./json-fg";

function SurveyComponent( {experiment_type}) {

    console.log(experiment_type);
    
    if (experiment_type === "h") {
        var json = json_h;
    } else if (experiment_type === "fg") {
        var json = json_fg;
    }

    const survey = new Model(json);
    survey.applyTheme(SurveyTheme.PlainLight);

    var ground_truth_matrix = survey.getQuestionByName("ground_truth_matrix");

    survey.onCurrentPageChanged.add(function (sender, options) {
        for (var i = 0; i < ground_truth_matrix.rows.length; i++) {
            let question = survey.getQuestionByName("question_" + (i + 1));
            let question_value = question?.value;
            let row_value = ground_truth_matrix.getRowValue(i);
            ground_truth_matrix.setRowValue(i, { "answer_column": question_value, "ground_truth_column": row_value?.ground_truth_column });
        }
    });

    survey.onComplete.add((sender, options) => {
        console.log(JSON.stringify(sender.data, null, 3));
    });
    return (<Survey model={survey} />);
}

export default SurveyComponent;