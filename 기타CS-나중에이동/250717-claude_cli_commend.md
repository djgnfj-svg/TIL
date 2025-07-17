# 
참고 link : https://apidog.com/kr/blog/claude-code-cli-commands-kr/

## option

### 터미널에서 작업이 끝나면 알람울림
```
claude config set --global preferredNotifChannel terminal_bell
```

### 이전 작업부터 재시작
```
claude --continue
```

### 과거 세션 목록을 표시하여 재개할 세션을 선택할 수 있습니다.
```
claude --resume
```

## CMD

### CLAUDE.MD 만들어줌
프로젝트의 아키텍처, 종속성, 코딩 컨벤션과 같은 상위 수준 정보를 저장할 수 있는 곳입니다.
```
/init
```

### 현재 세션에서 초기화
```
/clear
```

### 컨텍스트 관리
현재 대화를 요약해서 주요 정보를 보전하면서 토큰감소
```
/compact
```

### 코드 리뷰어
풀리퀘나 특정 파일 검토
```
/review
```

## text
### 개요 요청
Claude에게 현재 프로젝트의 목적, 주요 기능 및 기술 스택을 포함한 상위 수준 개요를 제공하도록 요청합니다.
```
summarize this project
```


### 프로젝트 디렉토리 분석 폴더의 목적
Claude에게 프로젝트의 디렉토리 구조를 분석하고 각 폴더의 목적을 설명하도록 요청합니다.
```
explain the folder structure
```

### 특정 기능에 관련된 코드를 찾아달라고 요청가능
전체 코드베이스를 검색하고 사용자 인증을 담당하는 파일을 식별합니다.
```
find the files that handle user authentication
```

### 아키텍처 패턴을 식별
```
explain the main architecture patterns used here
```