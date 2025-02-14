USE employeedb;
CREATE TABLE IF NOT EXISTS CANDIDATES1 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    StudentName VARCHAR(30) NOT NULL,
    CollegeName VARCHAR(50) NOT NULL,
    Round1Marks FLOAT CHECK (Round1Marks BETWEEN 0 AND 10),
    Round2Marks FLOAT CHECK (Round2Marks BETWEEN 0 AND 10),
    Round3Marks FLOAT CHECK (Round3Marks BETWEEN 0 AND 10),
    TechnicalRoundMarks FLOAT CHECK (TechnicalRoundMarks BETWEEN 0 AND 20),
    TotalMarks FLOAT GENERATED ALWAYS AS (Round1Marks + Round2Marks + Round3Marks + TechnicalRoundMarks) STORED,
    Result ENUM('Selected', 'Rejected') GENERATED ALWAYS AS 
    (IF(Round1Marks + Round2Marks + Round3Marks + TechnicalRoundMarks >= 35, 'Selected', 'Rejected')) STORED,
    RankOfStudents INT
);
SELECT * FROM CANDIDATES1;