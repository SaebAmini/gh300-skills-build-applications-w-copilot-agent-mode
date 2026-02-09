import React, { useState, useEffect } from 'react';

function Teams() {
  const [teams, setTeams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const codespace = process.env.REACT_APP_CODESPACE_NAME;
    const apiUrl = codespace 
      ? `https://${codespace}-8000.app.github.dev/api/teams/`
      : 'http://localhost:8000/api/teams/';

    console.log('Fetching teams from:', apiUrl);

    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        console.log('Teams data:', data);
        // Handle both paginated (.results) and plain array responses
        const teamsData = data.results || data;
        setTeams(teamsData);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching teams:', error);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div className="container mt-5"><h2>Loading teams...</h2></div>;
  }

  return (
    <div className="container mt-5">
      <h2 className="mb-4">Teams</h2>
      <div className="table-responsive">
        <table className="table table-striped table-hover">
          <thead className="table-dark">
            <tr>
              <th>Team Name</th>
              <th>Captain ID</th>
              <th>Member Count</th>
            </tr>
          </thead>
          <tbody>
            {teams.map(team => (
              <tr key={team.id}>
                <td>{team.name}</td>
                <td>{team.captain_id}</td>
                <td>{team.member_count}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Teams;
