*** Settings ***
Documentation    Suite description
Library   Compare_Image.py
*** Variables ***
${image1path}   ${CURDIR}\\path_to_image1\\img1.png
${image2path}   ${CURDIR}\\path_to_image2\\img1.png
*** Test Cases ***
Test title
    ${passed}    Compare_Image    ${image1path}   ${image2path}
    Run Keyword If  not ${passed}  Fatal Error  Images are not matching
