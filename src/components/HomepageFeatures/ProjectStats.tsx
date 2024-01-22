
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faDocker } from '@fortawesome/free-brands-svg-icons';
import { faCodeFork, faLanguage, faStar, faUsers } from '@fortawesome/free-solid-svg-icons';

import Heading from '@theme/Heading';
import styles from '@site/src/pages/index.module.css';

import InvenTreeStats from '@site/src/data/stats.json';


const humanNumber = require("human-number");


/*
 * Function to render a single "stats" item with:
 * - An icon
 * - A value
 * - A label
 */
function ProjectStatsItem({icon, value, label}) {

    return (
      <div className="col col--4">
        <div className="text--center">
          <h3>
            <FontAwesomeIcon icon={icon} size='xl' />
            {humanNumber(value, n => Number.parseFloat(n).toFixed(1) * 1)}
          </h3>
          <p>{label}</p>
        </div>
      </div>
    );
  }
  
  
  export default function ProjectStats() {
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