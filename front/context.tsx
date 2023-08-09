'use client';

import { Dispatch, ReactNode, createContext, useReducer } from "react";

type VideoInfo = {
  channel_text: string;
  channel_url: string;
  published_time: string;
  thumbnail_360x202: string;
  thumbnail_720x404: string;
  title_label: string;
  title_text: string;
  video_length: string;
  video_url: string;
  view_count: string;
}

type ContextProps = {
  children: ReactNode;
}

type ContextState = {
  searchResult: VideoInfo[];
  isResultLoading: boolean;
  isResultLoadingError: boolean;
};

type ContextAction = {
  type: string;
  payload: any;
};

const initialState: ContextState = {
  searchResult: [],
  isResultLoading: false,
  isResultLoadingError: false,
};

const reducer = (state: ContextState, action: ContextAction) => {
  switch (action.type) {
    case "SET_SEARCH_RESULT":
      return { ...state, searchResult: action.payload };
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
