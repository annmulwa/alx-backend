#!/usr/bin/yarn dev
import { Queue, Job } from 'kue';

/**
 * Creates push notification jobs from the array of jobs field.
 * @param {Job[]} jobs
 * @param {Queue} queue
 */

export const createPushNotificationsJobs = (jobs, queue) => {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  for (const jobField of jobs) {
    const job = queue.create('push_notification_code_3', jobField);

    job
      .on('enqueue', () => {
        console.log('Notification job created:', job.id);
      })
      .on('complete', () => {
        console.log('Notification job', job.id, 'completed');
      })
      .on('failed attempt', (err) => {
        console.log('Notification job', job.id, 'failed:', err.message || err.toString());
      })
      .on('progress', (progress, _data) => {
        console.log('Notification job', job.id, `${progress}% complete`);
      });
    job.save();
  }
};

export default createPushNotificationsJobs;
