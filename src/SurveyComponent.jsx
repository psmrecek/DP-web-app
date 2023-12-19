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
        var i1h = 96000;
        var i2h = 35000;
        var i7h = 40000;

        var i1fg = 101000;
        var i2fg = 37000;
        var i7fg = 40000;
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

    var ground_truth_matrix = survey.getQuestionByName("ground_truth_matrix");

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