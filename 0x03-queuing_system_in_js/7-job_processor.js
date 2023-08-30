import kue from 'kue';

// Array of blacklisted phone numbers
const blacklistedNumbers = ['4153518780', '4153518781'];

// Function to send a notification
const sendNotification = (phoneNumber, message, job, done) => {
  // Set initial progress to 0
  job.progress(0, 100);

  if (blacklistedNumbers.includes(phoneNumber)) {
    // Fail the job if phone number is blacklisted
    const errorMessage = `Phone number ${phoneNumber} is blacklisted`;
    done(new Error(errorMessage));
  } else {
    // Update progress to 50% and log message
    job.progress(50, 100);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    done();
  }
};

// Create a Kue queue with concurrency
const queue = kue.createQueue({ concurrency: 2 });

// Process the jobs in the queue
queue.process('push_notification_code_2', 2, (job, done) => {
  const { phoneNumber, message } = job.data;
  sendNotification(phoneNumber, message, job, done);
});

// Log message when the queue is ready
queue.on('ready', () => {
  console.log('Queue is ready to process jobs');
});

