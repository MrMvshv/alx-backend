import kue from 'kue';

// Create a Kue queue
const queue = kue.createQueue();

// Create an object with job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account'
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData).save((err) => {
  if (!err) {
    console.log(`Notification job created: ${job.id}`);
  }
});

// Job completion event
job.on('complete', () => {
  console.log('Notification job completed');
});

// Job failure event
job.on('failed', () => {
  console.log('Notification job failed');
});
