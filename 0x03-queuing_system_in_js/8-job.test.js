import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job'; // Adjust the path accordingly

// Create a Kue queue in test mode
const queue = kue.createQueue({ testMode: true });

describe('createPushNotificationsJobs', () => {
  afterEach(() => {
    // Clear the queue and exit test mode
    queue.testMode.clear();
  });

  it('should create jobs in the queue', () => {
    const list = [
      {
        phoneNumber: '4153518780',
        message: 'This is the code 1234 to verify your account',
      },
      // ... other job objects
    ];

    createPushNotificationsJobs(list, queue);

    console.log('Number of jobs in queue:', queue.testMode.jobs.length);

    const expectedJobData = list.map(job => ({
      type: 'push_notification_code_3',
      data: job,
    }));

    console.log('Expected jobs:', expectedJobData);

    console.log('Actual jobs:', queue.testMode.jobs);

    expect(queue.testMode.jobs.length).to.equal(list.length);

    expect(queue.testMode.jobs).to.deep.include.members(expectedJobData);
  });

  // Add more test cases as needed
});
