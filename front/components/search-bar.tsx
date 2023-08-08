'use client';

import React, { useState, useRef, FormEvent, ChangeEvent, useContext } from 'react';
import { GlobalContext } from '@/context';
import styles from '../styles/components/search-bar.module.scss';

export default function SearchBar() {

  const { dispatch } = useContext(GlobalContext);

  const [youTubeChannelName, setYouTubeChannelName] = useState('');

  const formInputRef = useRef<HTMLInputElement>(null);

  const handleFormInputChange = (evt: ChangeEvent<HTMLInputElement>) => {
    setYouTubeChannelName(evt.target.value);
  }

  const handleFormSubmit = async (evt: FormEvent<HTMLFormElement>) => {
    evt.preventDefault();

    try {
      const response = await fetch(`${process.env.NEXT_PUBLIC_BACK_API_URL}/get_you_tube_by_channel/?channel_name=${youTubeChannelName}`);
      if (!response.ok) {
        throw new Error('Ошибка сети');
      }
      const { final_json } = await response.json();
      dispatch({ type: 'SET_SEARCH_RESULT', payload: final_json });
    } catch (error) {
      console.error("Произошла ошибка при получении данных:", error);
      return null;
    }
  }

  return (
    <div className={styles['form-wrapper']}>
      <form className={styles['form']} action='#' onSubmit={handleFormSubmit}>
        <label className={styles['form-label']}>Enter youtube channel name:</label>
        <div className={styles['form-container']}>
          <button className={styles['form-btn']} type="submit">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#657789" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" className="feather feather-search"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          </button>
          <div className={styles['form-input-wrapper']}>
            <input className={styles['form-input']} ref={formInputRef} onChange={handleFormInputChange} value={youTubeChannelName} placeholder="Here..."/>
          </div>
        </div>
      </form>
    </div>
  )
}
