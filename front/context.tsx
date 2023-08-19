'use client';

import { Dispatch, ReactNode, createContext, useReducer } from "react";

type SearchResult = {
  all_this_shit_is_beacuse_of_this_youtube_channel: string;
  videos_from_first_channel: ProvidedChannelVideo[];
  competitors_channels: string[];
  generated_ideas: IdeasList;
}

type ProvidedChannelVideo = {
  title: string;
  url: string;
  thumbnail: string;
}

type Idea = {
  titles: string[];
  description: string;
}

type IdeasList = {
  [key: string]: Idea;
}

type ContextProps = {
  children: ReactNode;
}

type ContextState = {
  searchResult: SearchResult;
  youtubeChannelName: string;
  isResultLoading: boolean;
  isResultLoadingError: boolean;
};

type ContextAction = {
  type: string;
  payload: any;
};

const initialState: ContextState = {
  searchResult: {
    all_this_shit_is_beacuse_of_this_youtube_channel: '',
    videos_from_first_channel: [],
    competitors_channels: [],
    generated_ideas: {}
  },
  youtubeChannelName: '',
  isResultLoading: false,
  isResultLoadingError: false,
};

const reducer = (state: ContextState, action: ContextAction) => {
  switch (action.type) {
    case "SET_SEARCH_RESULT":
      return { ...state, searchResult: action.payload };
    case "SET_YOUTUBE_CHANNEL_NAME":
      return { ...state, youtubeChannelName: action.payload };
    case "SET_IS_RESULT_LOADING":
      return { ...state, isResultLoading: action.payload };
    case "SET_IS_RESULT_LOADING_ERROR":
      return { ...state, isResultLoadingError: action.payload };
    default:
      return state;
  }
};

export const GlobalContext = createContext<{
  state: ContextState;
  dispatch: Dispatch<ContextAction>;
}>({
  state: initialState,
  dispatch: () => null
});

export const GlobalContextProvider = ({children}: ContextProps) => {
  const [state, dispatch] = useReducer(reducer, initialState);

  return (
    <GlobalContext.Provider value={{ state, dispatch }}>
      {children}
    </GlobalContext.Provider>
  );
};
