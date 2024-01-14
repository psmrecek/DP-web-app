import React, { useEffect } from "react";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
import "survey-core/defaultV2.min.css";
import * as SurveyTheme from "survey-core/themes";
import "./index.css";
import { json_h } from "./json-h";
import { json_fg } from "./json-fg";


function SurveyComponent({ experiment_type }) {

    // If running on localhost, use debug values
    if (window.location.href.includes("localhost")) {
        var i1h = 1000;
        var i2h = 1000;
        var i7h = 1000;

        var i1fg = 1000;
        var i2fg = 1000;
        var i7fg = 1000;
    } else {
        var i1h = 99000;
        var i2h = 42000;
        var i7h = 42000;

        var i1fg = 104000;
        var i2fg = 44000;
        var i7fg = 42000;
    }

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

    var elaboration_pages = [
        "elaboration_1_1",
        "elaboration_1_2",
        "elaboration_2_1",
        "elaboration_2_2",
        "elaboration_3_1",
        "elaboration_3_2",
        "elaboration_4_1",
        "elaboration_4_2",
        "elaboration_5_1",
        "elaboration_5_2"
    ];

    const survey = new Model(json);
    survey.applyTheme(SurveyTheme.PlainLight);

    useEffect(() => {
        // Function to be called when mutations are observed
        const observerCallback = (mutationsList, observer) => {
            for (let mutation of mutationsList) {
                if (mutation.type === 'childList') {
                    let timerElements = document.getElementsByClassName('sd-timer');
                    if (timerElements.length > 0) {
                        timerElements[0].style.display = 'none';
                        observer.disconnect(); // Stop observing after finding the element
                    }
                }
            }
        };

        // Create an observer instance linked to the callback function
        const observer = new MutationObserver(observerCallback);

        // Start observing the body for added nodes
        observer.observe(document.body, { childList: true, subtree: true });

        // Clean up the observer on component unmount
        return () => observer.disconnect();
    }, []);

    var ground_truth_matrix_1 = survey.getQuestionByName("ground_truth_matrix_1");
    var ground_truth_matrix_2 = survey.getQuestionByName("ground_truth_matrix_2");
    var ground_truth_matrix_3 = survey.getQuestionByName("ground_truth_matrix_3");
    var ground_truth_matrix_4 = survey.getQuestionByName("ground_truth_matrix_4");
    var ground_truth_matrix_5 = survey.getQuestionByName("ground_truth_matrix_5");
    var ground_truth_matrix_6 = survey.getQuestionByName("ground_truth_matrix_6");
    var ground_truth_matrix_7 = survey.getQuestionByName("ground_truth_matrix_7");
    var ground_truth_matrix_8 = survey.getQuestionByName("ground_truth_matrix_8");
    var ground_truth_matrix_9 = survey.getQuestionByName("ground_truth_matrix_9");
    var ground_truth_matrix_10 = survey.getQuestionByName("ground_truth_matrix_10");

    var list_of_ground_truth_matrices = [
        ground_truth_matrix_1,
        ground_truth_matrix_2,
        ground_truth_matrix_3,
        ground_truth_matrix_4,
        ground_truth_matrix_5,
        ground_truth_matrix_6,
        ground_truth_matrix_7,
        ground_truth_matrix_8,
        ground_truth_matrix_9,
        ground_truth_matrix_10
    ];

    survey.onCurrentPageChanged.add(function (sender, options) {

        var question_name = survey.currentPage.questions[0].name;

        const timerElement = document.getElementsByClassName(
            "sd-timer"
        )[0];

        if (elaboration_pages.includes(question_name)) {
            timerElement.style.display = "block";
        } else {
            timerElement.style.display = "none";
        }

        if (question_name === "instructions_1" || question_name === "instructions_2" || question_name === "instructions_7") {
            const nextButton = document.getElementsByClassName(
                "sd-navigation__next-btn"
            )[0];
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

        for (var matrix_index = 0; matrix_index < list_of_ground_truth_matrices.length; matrix_index++) {
            var ground_truth_matrix = list_of_ground_truth_matrices[matrix_index];
            var offset = 60 / list_of_ground_truth_matrices.length * matrix_index;

            for (var matrix_row_index = 0; matrix_row_index < ground_truth_matrix.rows.length; matrix_row_index++) {
                let question = survey.getQuestionByName("question_" + (matrix_row_index + offset + 1));
                let question_value = question?.value;
                let row_value = ground_truth_matrix.getRowValue(matrix_row_index);
                ground_truth_matrix.setRowValue(matrix_row_index, { "answer_column": question_value, "ground_truth_column": row_value?.ground_truth_column });
            }
        }
    });

    survey.onComplete.add((sender, options) => {
        console.log(JSON.stringify(sender.data, null, 3));
    });
    return (<Survey model={survey} />);
}

export default SurveyComponent;