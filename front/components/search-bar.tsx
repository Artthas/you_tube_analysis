'use client';

import React, { useState, useRef, FormEvent, ChangeEvent } from 'react';
import styles from '../styles/components/search-bar.module.scss';

export default function SearchBar() {

  const [youTubeLink, setYouTubeLink] = useState('');

  const formInputRef = useRef<HTMLInputElement>(null);

  const handleFormInputChange = (evt: ChangeEvent<HTMLInputElement>) => {
    setYouTubeLink(evt.target.value);
  }

  const handleFormSubmit = (evt: FormEvent<HTMLFormElement>) => {
    evt.preventDefault();
  }

  return (
    <div className={styles['form-wrapper']}>
      <form className={styles['form']} action='#' onSubmit={handleFormSubmit}>
        <label className={styles['form-label']}>Insert link to youtube channel:</label>
        <div className={styles['form-container']}>
          <button className={styles['form-btn']} type="submit">
            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="#657789" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round" className="feather feather-search"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          </button>
          <div className={styles['form-input-wrapper']}>
            <input className={styles['form-input']} ref={formInputRef} onChange={handleFormInputChange} value={youTubeLink} placeholder="Here..."/>
          </div>
        </div>
      </form>
    </div>
  )
}
