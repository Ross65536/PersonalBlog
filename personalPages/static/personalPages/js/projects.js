'use strict';

const ACTIVE_BUTTON_CLASSNAME = "active";
const CARD_DISPLAY_VALUE = "inline-block";

class TagManager {
    constructor() {
        this._activeTags = [];
    }

    toggleActiveTag(tagName) {
        const index = this._activeTags.indexOf(tagName);
        if(index >= 0) {
            this._activeTags.splice(index, 1);
        } 
        else {
            this._activeTags.push(tagName);
        }
    }

    get tags() {
        return this._activeTags;
    }

    get isEmpty() {
        return this._activeTags.length == 0;
    }

    get length() {
        return this._activeTags.length;
    }

    containsTag(tagName) {
        const index = this._activeTags.indexOf(tagName);
        return index >= 0;
    }
}



const buttons = $('.card button');
const tagManager = new TagManager();

function toggleCards() {
    const cards = $('.card');

    if(tagManager.isEmpty) {
        cards.each((index, card) => {
            card.style.display = CARD_DISPLAY_VALUE;
        });

        buttons.each((index, button) => {
            button.classList.remove(ACTIVE_BUTTON_CLASSNAME);
        });
    }
    else 
        cards.each((index, card) => {
            const buttons = card.getElementsByTagName('button');
            let activeCount = 0;
            for(const button of buttons) {
                const tagName = button.innerHTML;
                if(tagManager.containsTag(tagName)) {
                    activeCount += 1;
                    button.classList.add(ACTIVE_BUTTON_CLASSNAME);
                }
                else {
                    button.classList.remove(ACTIVE_BUTTON_CLASSNAME);
                }
            }
            if(tagManager.length != activeCount)
                card.style.display = "none";
            else 
                card.style.display = CARD_DISPLAY_VALUE;
        });
}


buttons.click((eventObject) => {
    const button = eventObject.currentTarget;
    const buttonText = button.innerHTML;
    
    tagManager.toggleActiveTag(buttonText);
    console.log(tagManager.tags);
    toggleCards();

})