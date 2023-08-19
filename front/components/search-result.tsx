'use client';

import React, { useContext } from 'react';
import { GlobalContext } from '@/context';
import Image from 'next/image';
import Link from 'next/link';
import styles from '../styles/components/search-result.module.scss';
import Loading from './loading';

export default function SearchResult() {

  const { state: { searchResult, isResultLoading, isResultLoadingError } } = useContext(GlobalContext);

  if (isResultLoading) {
    return <Loading />;
  }

  if (isResultLoadingError) {
    return <div className={styles['error-message']}>An error occurred while loading the results. Please try again.</div>;
  }

  if (!searchResult.all_this_shit_is_beacuse_of_this_youtube_channel) {
    return <></>;
  }

  return (
    <section className={styles['main']}>
      {/* <ul className={styles['main-video-list']}>
        {searchResult.videos_from_first_channel.map((item) =>
          <li className={styles['main-video-item']} key={item?.url}>
            <div className={styles['main-video-item-wrapper']}>
              <Link className={styles['main-video-link']} href={item?.url}>
                <Image
                  className={styles['main-video-image']}
                  src={item?.thumbnail}
                  width={250}
                  height={150}
                  alt="Preview"
                />
                <p className={styles['main-video-title']}>{item.title}</p>
              </Link>
            </div>
          </li>
        )}
      </ul> */}
      <ul className={styles['main-idea-list']}>
        {Object.values(searchResult.generated_ideas).map((item) =>
          <li className={styles['main-idea-item']} key={item?.description}>
            <div className={styles['main-idea-item-wrapper']}>
              <p>Titles:</p>
              <p>{item.titles.map((str) => <span key={str}>- {str}</span>)}</p>
              <p>Description:</p>
              <p>{item.description}</p>
            </div>
          </li>
        )}
      </ul>
    </section>
  );
}
