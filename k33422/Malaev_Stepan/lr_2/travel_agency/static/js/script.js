"use strict";


// Typing effect

const words = [
    "journey through the Amazon Rainforest",
    "cultural exploration in Kyoto",
    "historical quest to the Pyramids of Giza",
    "culinary adventure to Tuscany",
    "wine tasting in Napa Valley",
    "art tour in the Louvre, Paris",
    "diving trip to the Great Barrier Reef",
    "pilgrimage to Santiago de Compostela",
    "wildlife expedition in the Galapagos Islands",
    "ski escape to the Alps",
];

const TYPING_SPEED = 80;
const DELETING_SPEED = 35;
const DELAY_BETWEEN_WORDS = 2000;

function typeEffect($dynamicText, wordIndex = 0, charIndex = 0, isDeleting = false) {
    const currentWord = words[wordIndex];

    $dynamicText.text(currentWord.substring(0, charIndex));
    $dynamicText.toggleClass("stop-blinking", isDeleting);

    if (!isDeleting && charIndex < currentWord.length) {
        charIndex++;
        setTimeout(() => typeEffect($dynamicText, wordIndex, charIndex, isDeleting), TYPING_SPEED);
    } else if (isDeleting && charIndex > 0) {
        charIndex--;
        setTimeout(() => typeEffect($dynamicText, wordIndex, charIndex, isDeleting), DELETING_SPEED);
    } else {
        isDeleting = !isDeleting;
        $dynamicText.removeClass("stop-blinking");
        wordIndex = !isDeleting ? (wordIndex + 1) % words.length : wordIndex;
        setTimeout(() => typeEffect($dynamicText, wordIndex, charIndex, isDeleting), DELAY_BETWEEN_WORDS);
    }
}


// Status Loader

function createStatusMessageHandler(formSelector) {
    const $form = $(`${formSelector}`);
    const $circleLoader = $form.find('.circle-loader');
    const $messageObject = $form.find('.message');

    return {
        show: function (status, statusMessage = '') {
            $circleLoader.show().removeClass().addClass(`circle-loader ${status}`);
            $messageObject.removeClass('error-message success-message');

            if (status) {
                const messageClass = status === 'failed' ? 'error-message' : 'success-message';
                $messageObject.addClass(messageClass).text(statusMessage).show();
            } else {
                $messageObject.hide();
            }
        },
        hide: function () {
            $circleLoader.hide();
            $messageObject.hide();
        }
    };
}


// Form Handler

const DEFAULT_ERROR_MESSAGE = 'Unknown error. Try again.';
const SUCCESS_MESSAGE = 'Success!';
const RELOAD_TIMEOUT = 650;

function createFormHandler(formSelector, url) {
    return async (event) => {
        event.preventDefault();

        const statusHandler = createStatusMessageHandler(formSelector);
        const $submitButton = $(`${formSelector} button[type="submit"]`);

        try {
            statusHandler.show('');
            $submitButton.prop('disabled', true);

            const response = await $.ajax({
                url: url,
                type: 'post',
                data: $(formSelector).serialize()
            });

            const message = response?.success ? SUCCESS_MESSAGE : DEFAULT_ERROR_MESSAGE;
            statusHandler.show(response?.success ? 'success' : 'failed', message);

            if (response?.success) {
                setTimeout(() => location.reload(), RELOAD_TIMEOUT);
            }
        } catch (error) {
            const errorMessage = error.responseJSON?.error || DEFAULT_ERROR_MESSAGE;
            statusHandler.show('failed', errorMessage);
        } finally {
            $submitButton.prop('disabled', false);
        }
    };
}

$(document).ready(function () {
    $('.dropdown-trigger').dropdown();

    M.Modal.init($('.modal'), {
        onCloseEnd: function () {
            $('.modal-content form').trigger("reset");
            createStatusMessageHandler('.modal-content form').hide()
        }
    });

    $('#login-form').on('submit', createFormHandler('#login-form', DjangoConfig.LOGIN_URL));
    $('#register-form').on('submit', createFormHandler('#register-form', DjangoConfig.REGISTER_URL));

    $('.logout-link').on('click', function (event) {
        event.preventDefault();
        $('#logout-form').submit();
    });

    const dynamicText = $(".dynamic-header span");
    if (dynamicText) {
        typeEffect(dynamicText);
    }
});
