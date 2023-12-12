import React, { useState } from "react";
import { Model } from "survey-core";
import { Survey } from "survey-react-ui";
import "survey-core/defaultV2.min.css";
import * as SurveyTheme from "survey-core/themes";
import "./index.css";
import { json } from "./json";

function SurveyComponent() {
    const survey = new Model(json);
    survey.applyTheme(SurveyTheme.PlainLight);
    // ---------------------------------------------------------------------------------------------


    // // Global variable to keep track of time
    // const [timeFlag, setTimeFlag] = useState(false);

    // var seconds = 0;
    // // Print time from timer to console
    // survey.onTimer.add(function (sender, options) {
    //     seconds++;

    //     if (seconds % 5 === 0) {
    //         setTimeFlag(true);
    //     }
    // });

    // -----------------------------------------------

    // // Add button
    // survey.addNavigationItem({
    //     id: "sv-nav-clear-page",
    //     title: "Clear Page",
    //     action: () => {
    //         survey.currentPage.questions.forEach((question) => {
    //             question.value = undefined;
    //         });
    //     },
    //     css: "nav-button",
    //     innerCss: "sd-btn nav-input"
    // });

    // -----------------------------------------------

    const [pageNo, setPageNo] = React.useState(survey.currentPageNo);
    const [isRunning, setIsRunning] = React.useState(true);
    survey.onCurrentPageChanged.add((_, options) => {
        setPageNo(options.newCurrentPage.visibleIndex);
    });
    survey.onStarted.add(() => { setIsRunning(true); });
    survey.onComplete.add(() => { setIsRunning(false); });
    survey.onComplete.add((sender, options) => {
        console.log(JSON.stringify(sender.data, null, 3));
    });
    const nextPage = () => { survey.nextPage(); };
    const endSurvey = () => { survey.completeLastPage(); };

    const renderButton = (text, func, canRender) => {
        if (!canRender) return undefined;
        return (
            <button className="navigation-button" onClick={func}>
                {text}
            </button>
        );
    };

    const renderExternalNavigation = () => {
        if (!isRunning) return undefined;
        return (
            <div className="navigation-block">
                <div className="navigation-buttons-container">
                    {renderButton('Next', nextPage, pageNo !== survey.visiblePages.length - 1)}
                    {renderButton('Complete', endSurvey, pageNo === survey.visiblePages.length - 1)}
                </div>
            </div>
        );
    };

    // ---------------------------------------------------------------------------------------------
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
    // return (<Survey model={survey} />);
    return (
        <div>
            <Survey
                currentPageNo={pageNo}
                model={survey}
            />
            {renderExternalNavigation()}

        </div>
    );
}

export default SurveyComponent;