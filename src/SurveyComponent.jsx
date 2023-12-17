import React, { useEffect } from "react";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
import "survey-core/defaultV2.min.css";
import * as SurveyTheme from "survey-core/themes";
import "./index.css";
import { json_h } from "./json-h";
import { json_fg } from "./json-fg";

function SurveyComponent({ experiment_type }) {

    var i1h = 5000;
    var i2h = 7000;
    var i7h = 10000;

    var i1fg = 10000;
    var i2fg = 5000;
    var i7fg = 7000;

    console.log(experiment_type);

    if (experiment_type === "h") {
        var json = json_h;
    } else if (experiment_type === "fg") {
        var json = json_fg;
    }

    // Disable next button on first
    useEffect(() => {
        const nextButton = document.getElementsByClassName(
            "sd-navigation__next-btn"
        )[0];
        console.log(nextButton);
        nextButton.disabled = true;

        if (experiment_type === "h") {
            setTimeout(() => {
                nextButton.disabled = false;
            }, i1h);
        }

        if (experiment_type === "fg") {
            setTimeout(() => {
                nextButton.disabled = false;
            }, i1fg);
        }

    }, []);

    const survey = new Model(json);
    survey.applyTheme(SurveyTheme.PlainLight);

    var ground_truth_matrix = survey.getQuestionByName("ground_truth_matrix");

    survey.onCurrentPageChanged.add(function (sender, options) {

        var question_name = survey.currentPage.questions[0].name;

        if (question_name === "instructions_1" || question_name === "instructions_2" || question_name === "instructions_7") {
            const nextButton = document.getElementsByClassName(
                "sd-navigation__next-btn"
            )[0];
            console.log(nextButton);
            nextButton.disabled = true;

            if (question_name === "instructions_1" && experiment_type === "h") {
                setTimeout(() => {
                    nextButton.disabled = false;
                }, i1h);
            }

            if (question_name === "instructions_2" && experiment_type === "h") {
                setTimeout(() => {
                    nextButton.disabled = false;
                }, i2h);
            }

            if (question_name === "instructions_7" && experiment_type === "h") {
                setTimeout(() => {
                    nextButton.disabled = false;
                }, i7h);
            }

            if (question_name === "instructions_1" && experiment_type === "fg") {
                setTimeout(() => {
                    nextButton.disabled = false;
                }, i1fg);
            }

            if (question_name === "instructions_2" && experiment_type === "fg") {
                setTimeout(() => {
                    nextButton.disabled = false;
                }, i2fg);
            }

            if (question_name === "instructions_7" && experiment_type === "fg") {
                setTimeout(() => {
                    nextButton.disabled = false;
                }, i7fg);
            }
        }

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