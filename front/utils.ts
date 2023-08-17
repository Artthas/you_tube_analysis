type DispatchType = (action: { type: string, payload: any }) => void;
type MockDataType = { final_json: any };

export const simulateReqServer = (dispatch: DispatchType, mockData: MockDataType) => {
  const { final_json } = mockData;
  dispatch({ type: 'SET_IS_RESULT_LOADING', payload: true });
  setTimeout(() => {
      dispatch({ type: 'SET_IS_RESULT_LOADING', payload: false });
      dispatch({ type: 'SET_YOUTUBE_CHANNEL_NAME', payload: 'rapdailyofficial' });
      dispatch({ type: 'SET_SEARCH_RESULT', payload: final_json });
  }, 1000);
}