import React, { useState, useEffect } from 'react';

function Workouts() {
  const [workouts, setWorkouts] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/workouts/`
      : 'http://localhost:8000/api/workouts/';

    console.log('Fetching workouts from:', apiUrl);

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Workouts data:', data);
        // Handle both paginated (.results) and plain array responses
        const workoutsData = data.results || data;
        setWorkouts(workoutsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching workouts:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="container mt-5"><h2>Loading workouts...</h2></div>;
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Workout Suggestions</h2>
      <div className="row">
        {workouts.map(workout => (
          <div key={workout.id} className="col-md-6 col-lg-4 mb-4">
            <div className="card h-100">
              <div className="card-body">
                <h5 className="card-title">{workout.name}</h5>
                <p className="card-text">{workout.description}</p>
                <ul className="list-group list-group-flush">
                  <li className="list-group-item"><strong>Difficulty:</strong> {workout.difficulty}</li>
                  <li className="list-group-item"><strong>Duration:</strong> {workout.duration} mins</li>
                  <li className="list-group-item"><strong>Type:</strong> {workout.type}</li>
                  <li className="list-group-item"><strong>Calories:</strong> ~{workout.calories_estimate}</li>
                </ul>
              </div>
              <div className="card-footer">
                <button className="btn btn-primary btn-sm w-100">Start Workout</button>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default Workouts;
