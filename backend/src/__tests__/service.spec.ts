import {EsolangService} from "../service/esolang.service";

describe('Demo service test', () => {
    test('sum of a and b should work', () => {
        const result = EsolangService.sum(5, 7);

        expect(result).toEqual(12);
    });
});
