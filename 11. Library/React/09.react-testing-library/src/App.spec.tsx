import { render, screen, fireEvent } from "@testing-library/react"
import App from './App'

describe('<App />', () => {
  describe('테스트1', () => {
    it('텍스트 렌더 확인', () => {
      render(<App />);
      const linkElement = screen.getByText(/Learn react/i);
      expect(linkElement).toBeInTheDocument();
    })

    it('링크가 클릭되면 "clicked" 텍스트가 보임', () => {
      render(<App />);
      const linkElement = screen.getByText(/Learn react not clicked/i);

      // true인지 판별
      expect(fireEvent.click(linkElement)).toBeTruthy();
      expect(screen.getByText(/Learn react clicked/i)).toBeInTheDocument();
    })

    it('up/down이 클릭되면 카운트값이 변동', () => {
      render(<App />);
      const up = screen.getByText('up');
      const down = screen.getByText('down');

      fireEvent.click(up);
      expect(screen.getByText('Count is 1')).toBeInTheDocument();

      fireEvent.click(up);
      expect(screen.getByText('Count is 2')).toBeInTheDocument();
      
      fireEvent.click(down);
      expect(screen.getByText('Count is 1')).toBeInTheDocument();
    })

  })
})