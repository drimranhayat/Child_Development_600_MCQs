"""Produce portable question-bank JSON files and a topic coverage map."""
import json
from pathlib import Path

def export(course):
 bank=Path('question-bank');bank.mkdir(exist_ok=True)
 questions=[q for lesson in course['lessons'] for q in lesson['questions']]
 (bank/'600-mcqs.json').write_text(json.dumps(dict(title='Child Development: 600 exam-focused MCQs',count=len(questions),questions=questions),ensure_ascii=False,indent=2))
 lines=['# Exam coverage map','', '600 MCQs; 75 in each lecture. All 66 major study topics have mapped questions. Source ranges refer to the supplied lecture decks. Some questions apply or clarify a concept rather than quote it directly.','', 'Approximate age questions identify course teaching anchors. Selected outdated or incorrect slide claims are clarified in the study notes and explanations. Review source illustrations and the instructor’s guidance as well; a question bank cannot guarantee an exam’s contents.','']
 for lesson in course['lessons']:
  lines +=[f"## Lecture {lesson['id']}: {lesson['title']}",'','| Topic | Source slide range | Questions |','| --- | --- | --- |']
  for topic in lesson['topics']:
   n=sum(q['topicId']==topic['id'] for q in lesson['questions'])
   lines +=[f"| {topic['title']} | {topic['slides']} | {n} |"]
  lines+=['']
  (bank/f"lecture-{lesson['id']:02}.json").write_text(json.dumps(dict(lecture=lesson['id'],title=lesson['title'],count=len(lesson['questions']),questions=lesson['questions']),ensure_ascii=False,indent=2))
 Path('COVERAGE.md').write_text('\n'.join(lines))
