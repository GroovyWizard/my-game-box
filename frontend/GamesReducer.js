import { combineReducers } from 'redux';

const INITIAL_STATE = {
  current: [],
  possible: [
    1,
    2,
    3,
  ],
};

const gamesReducer = (state = INITIAL_STATE, action) => {
  switch (action.type) {
    case 'ADD_GAME':
        const {
            current,
            possible,
        } = state;

        const addedGame = possible.splice(action.payload, 1);

        current.push(addedGame);

        const newState = { current, possible };
        
        return newState;
        
        default:
            return state
    }
};

export default combineReducers({
  games: gamesReducer
});