import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';
import Heading from '@theme/Heading';


import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDocker } from '@fortawesome/free-brands-svg-icons';
import { faCodeFork, faLanguage, faStar, faUsers } from '@fortawesome/free-solid-svg-icons';

import { InvenTreeStats } from '@site/src/components/HomepageFeatures/stats';
import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/intro">
            Docusaurus Tutorial - 5min ⏱️
          </Link>
        </div>
      </div>
    </header>
  );
}


function ProjectStatsItem({icon, value, label}) {

  return (
    <div className="col col--4">
      <div className="text--center">
        <h3>
          <FontAwesomeIcon icon={icon} size='xl' />
          {value}
        </h3>
        <p>{label}</p>
      </div>
    </div>
  );
}


function ProjectStats() {
  return (
    <section className={styles.projectStats}>
      <div className="container">
        <Heading as="h2">Harness the power of open source</Heading>
        <p>
          InvenTree is an open source project built by a community of developers.
        </p>
        <div className="row">
          <ProjectStatsItem icon={faDocker} value={InvenTreeStats.docker_pulls} label="Docker Pulls" />
          <ProjectStatsItem icon={faUsers} value={InvenTreeStats.github_contributors} label="Contributors" />
          <ProjectStatsItem icon={faCodeFork} value={InvenTreeStats.github_forks} label="GitHub Forks" />
          <ProjectStatsItem icon={faStar} value={InvenTreeStats.github_stars} label="GitHub Stars" />
          <ProjectStatsItem icon={faLanguage} value={InvenTreeStats.crowdin_languages} label="Supported Languages" />
        </div>
      </div>
    </section>
  );
}


export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="InvenTree - Intuitive Inventory Management">
      <HomepageHeader />
      <main>
        <HomepageFeatures />
        <ProjectStats />
      </main>
    </Layout>
  );
}
